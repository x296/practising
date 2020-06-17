import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class MyClass {
	public static void main(String[] args) {
		BankAccount account = new BankAccount("Jan Kowalski", 1);
		account.showMenu();
	}
}

class BankAccount {
	int balance;
	String previousTransaction;
	String customerName;
	int customerId;
	List<String> transactionHistory = new ArrayList<String>();

	BankAccount(String cname, int cid) {
		customerName = cname;
		customerId = cid;
	}

	void setName(String cname) {
		customerName = cname;
		transactionHistory.add("Name changed to "+cname);
	}

	void deposit(int amount) {
		if(amount != 0) {
			balance = balance + amount;
			String forPrevioustransaction = Integer.toString(amount);
			previousTransaction = "Deposited: "+forPrevioustransaction;
			transactionHistory.add(previousTransaction);
		}
	}

	void withdraw(int amount) {
		if(amount != 0) {
			balance = balance - amount;
			String forPrevioustransaction = Integer.toString(amount);
			previousTransaction = "Withdrawn: "+forPrevioustransaction;
			transactionHistory.add(previousTransaction);
		}
	}

	void donate(int amount, String charity) {
		if(amount != 0) {
			balance = balance - amount;
			String forPrevioustransaction = Integer.toString(amount);
			previousTransaction = "Donated "+forPrevioustransaction+" for "+charity;
			transactionHistory.add(previousTransaction);
		}
	}

	void getPreviousTransaction() {
		if(previousTransaction != null) {
			System.out.println(previousTransaction);
		}
		else {
			System.out.println("No transaction occured.");
		}
	}

	void getHistoryOfTransactions() {
		for(int i=0; i<transactionHistory.size(); i++) {
			System.out.println(transactionHistory.get(i));
		}
	}

	void showMenu() {
		char option = '\0';
		Scanner scanner = new Scanner(System.in);

		System.out.println("Welcome, Your ID is "+customerId);
		System.out.println("\n");
		System.out.println("A. Set customer name");
		System.out.println("B. View customer name");
		System.out.println("C. Check Balance");
		System.out.println("D. Deposit");
		System.out.println("E. Withdraw");
		System.out.println("F. Donate");
		System.out.println("G. Previous transaction");
		System.out.println("H. Show history");
		System.out.println("I. Exit");

		do {
			System.out.println("***********************************************");
			System.out.println("Enter an option");
			System.out.println("***********************************************");
			option = scanner.next().charAt(0);
			System.out.println("\n");

			switch(option) {
				case 'A':
					System.out.println("-----------------------------------------------");
					System.out.println("Enter customer name: ");
					System.out.println("-----------------------------------------------");
					scanner.nextLine();
					String newName = scanner.nextLine();
					setName(newName);
					System.out.println("\n");
					break;

				case 'B':
					System.out.println("-----------------------------------------------");
					System.out.println("Your name is: "+customerName);
					System.out.println("-----------------------------------------------");
					System.out.println("\n");
					break;

				case 'C':
					System.out.println("-----------------------------------------------");
					System.out.println("Balance = "+balance);
					System.out.println("-----------------------------------------------");
					System.out.println("\n");
					break;

				case 'D':
					System.out.println("-----------------------------------------------");
					System.out.println("Enter an amount to deposit: ");
					System.out.println("-----------------------------------------------");
					int amount = scanner.nextInt();
					deposit(amount);
					System.out.println("\n");
					break;

				case 'E':
					System.out.println("-----------------------------------------------");
					System.out.println("Enter an amount to withdraw: ");
					System.out.println("-----------------------------------------------");
					int amount2 = scanner.nextInt();
					withdraw(amount2);
					System.out.println("\n");
					break;

				case 'F':
					System.out.println("-----------------------------------------------");
					System.out.println("Enter amount of donation: ");
					System.out.println("-----------------------------------------------");
					int amount3 = scanner.nextInt();
					System.out.println("-----------------------------------------------");
					System.out.println("Enter name of charity, which you want bestow: ");
					System.out.println("-----------------------------------------------");
					scanner.nextLine();
					String charname = scanner.nextLine();
					donate(amount3, charname);
					System.out.println("\n");
					break;

				case 'G':
					System.out.println("-----------------------------------------------");
					getPreviousTransaction();
					System.out.println("-----------------------------------------------");
					System.out.println("\n");
					break;

				case 'H':
					System.out.println("-----------------------------------------------");
					System.out.println("History of operations: ");
					System.out.println("-----------------------------------------------");
					getHistoryOfTransactions();
					System.out.println("\n");
					break;

				case 'I':
					System.out.println("***********************************************");
					break;

				default:
					System.out.println("Invalid Option! Please enter again.");
			}
		} while(option != 'I');
		System.out.println("Thank You for using our services!");
	}
}
