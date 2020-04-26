import os
from pytube import YouTube

# Creating output name of downloading file
def creatingOutputFileName(srcString, outputExt):

	specialCharacters = ['|', '&', ':', ';', '(', ')', '<', '>', '~', '*', '@', '?', '!', '$', '#', '[', ']', '{', '}', '\\', '/', '\'', '\"', '`', ' ']

	fileName = 'out/'
	
	for letter in srcString:
		if letter in specialCharacters:
			fileName += '\\'
		fileName += letter

	if outputExt == 'mp4':
		fileName += '.mp4'
	elif outputExt == 'mp3':
		fileName += '.mp3'
	
	return fileName

print('Welcome to simple YouTube Downloader!\n')

# Pasting url adress
userUrl = input('Please paste here to YouTube video url you want to download: ')

print("\nloading...\n")

ytFile = YouTube(userUrl)

try:
	# Choosing between mp3 and mp4
	userOutputFileType = str(input('Wanna download a video or mp3 file? '))

	if userOutputFileType == 'video':

		# Printing available resolutions and choosing one
		print('Available resolutions')
		for i, stream in zip(range(len(ytFile.streams.filter(adaptive=True, mime_type='video/mp4'))), reversed(ytFile.streams.filter(adaptive=True, mime_type='video/mp4').order_by('resolution'))):
			print(i + 1, stream.resolution)

		userResolution = int(input('Type picked resolution number (1-{}): '.format(len(ytFile.streams.filter(adaptive=True, mime_type='video/mp4').order_by('resolution')))))

		print("\ndownloading...\n")

		# Downloading src files
		ytFile.streams.filter(adaptive=True, mime_type='video/mp4').order_by('resolution')[-2 + userResolution].download(output_path='src', filename='video')
		ytFile.streams.filter(adaptive=True, mime_type='audio/mp4').order_by('abr')[-1].download(output_path='src', filename='audio')

		# Merging audio and video via ffmpeg
		os.system('ffmpeg -i {} -i {} -c copy {}'.format('src/video.mp4', 'src/audio.mp4', creatingOutputFileName(ytFile.title, 'mp4')))

		# Optionally removing src files
		deleteSrcFiles = input('Do you want to delete source files? [y/N] ')
		if deleteSrcFiles == 'y':
			os.system('rm {} {}'.format('src/video.mp4', 'src/audio.mp4'))
		elif deleteSrcFiles != 'N':
			print('\nYou typed a wrong answer and your src files will be deleted.')
			os.system('rm {} {}'.format('src/video.mp4', 'src/audio.mp4'))

	elif userOutputFileType == 'mp3':
		# Downloading src file
		ytFile.streams.filter(adaptive=True, mime_type='audio/mp4').order_by('abr')[-1].download(output_path='src', filename='audio')

		# Converting mp4 to mp3 via ffmpeg
		os.system('ffmpeg -i {} {}'.format('src/audio.mp4', creatingOutputFileName(ytFile.title, 'mp3')))

		# Optionally removing src files
		deleteSrcFiles = input('Do you want to delete source files? [y/N] ')
		if deleteSrcFiles == 'y':
			os.system('rm {}'.format('src/audio.mp4'))
		elif deleteSrcFiles != 'N':
			print('\nYou typed a wrong answer and your src files will be deleted.')
			os.system('rm {}'.format('src/audio.mp4'))

	else:
		print('You probably misstyped an answer...')

except Exception as error:
	print(error)
