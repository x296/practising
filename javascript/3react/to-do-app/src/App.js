import React from 'react'
import ToDoItem from './components/ToDoItem'
import todoData from './components/todoData'

class App extends React.Component {
	constructor() {
		super()
		this.state = {
			todos: todoData
		}
		this.handleChange = this.handleChange.bind(this)
	}

	handleChange(id) {
		this.setState(prevState => {
			const updatedTodos = prevState.todos.map(todo => {
				if (todo.id === id) {
					todo.completed = !todo.completed
				}
				return todo
			})
			return {
				todos: updatedTodos
			}
		})
	}

	render() {
		const tasksComponents = this.state.todos.map(item => <ToDoItem key={item.id} item={item} handleChange={this.handleChange}/>)
		return (
			<div className='todo-list'>
				{tasksComponents}
			</div>
		)
	}
}

export default App