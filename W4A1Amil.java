package activities;

import java.util.*;

public class W4A1Amil {
	static void Amiladd(int first, int second) {
		int sum = first + second;
		System.out.print("Sum is: " + sum);
	}
	static void Amilminus(int first, int second) {
		int difference = first - second;
		System.out.print("Difference is: " + difference);
	}
	static void Amiltimes(int first, int second) {
		int product = first * second;
		System.out.print("Product is: " + product);
	}
	static void Amildivide(int first, int second) {
		int quotient = first / second;
		System.out.print("Quotient is: " + quotient);
	}

	static void Amilmenu() {
		System.out.println("Enter operation type: 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division ");
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner (System.in);
		Amilmenu();
		int operation = scanner.nextInt();
		System.out.print("Enter first number: ");
		int first = scanner.nextInt();
		System.out.print("Enter second number: ");
		int second = scanner.nextInt();
		
		if (operation == 1) {
			Amiladd(first, second);
		}
		else if (operation == 2) {
			Amilminus(first, second);
		}
		else if (operation == 3) {
			Amiltimes(first, second);
		}
		else if (operation == 4) {
			Amildivide(first, second);
		}
		else {
			System.out.print("Invalid operation type");
		}
	}

}
