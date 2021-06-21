import java.util.Scanner;
import java.util.Arrays;

/*
Input: hne_anecnt_sye_idi__wmioswaemnihs_e?
*/

public class Multidimensional {
	
	private char[][] arr;
	private String mrConnolly;
	
	public Multidimensional(String s) {
		arr = new char[6][6];
		for (int i = 0; i < s.length(); i++) {
			arr[i % 6][i / 6] = s.charAt(i);
		}
		for (int row = 0; row < arr.length; row++) {
			for (int col = 0; col < arr[row].length; col++) {
				System.out.printf("%5c", arr[row][col]);
			}
			System.out.println();
		}
		System.out.println();
		mrConnolly = "hey_since_when_was_time_a_dimension?";
	}
	
	public boolean check() {
		String s = "";
		for (char[] row: arr)
			for (char c: row)
				s += c;
		System.out.println(s);
		return s.equals(mrConnolly);
	}

	public void line_old() {
		char[][] newArr = new char[arr.length][arr[0].length];
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[0].length; j++) {
				int p = i - 1, q = j - 1, f = 0;
				boolean row = i % 2 == 0;
				boolean col = j % 2 == 0;
				if (row) {
					p = i + 1;
					f++;
				} else
					f--;
				if (col) {
					q = j + 1;
					f++;
				} else
					f--;
				newArr[p][q] = (char) (arr[i][j] + f);
			}
		}
		arr = newArr;
	}

	public void line() {
		char[][] newArr = new char[arr.length][arr[0].length];
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[0].length; j++) {
				int p = i - 1, q = j - 1, f = 0;
				boolean row = i % 2 == 0;
				boolean col = j % 2 == 0;
				if (row) {
					p = i + 1;
					f--;
				} else
					f++;
				if (col) {
					q = j + 1;
					f--;
				} else
					f++;
				newArr[p][q] = (char) (arr[i][j] - f);
			}
		}
		arr = newArr;
		/*
		for (int row = 0; row < newArr.length; row++) {
			for (int col = 0; col < newArr[row].length; col++) {
				System.out.printf("%5c", newArr[row][col]);
			}
			System.out.println();
		}
		System.out.println();
		arr = newArr;
		*/
	}

	public void plane_old() {
		int n = arr.length;
		for (int i = 0; i < n / 2; i++) {
			for (int j = 0; j < n / 2; j++) {
				char t = arr[j][n - 1 -i];
				arr[j][n - 1 -i] = arr[n - 1 - i][n - 1 - j];
				arr[n - 1 - i][n - 1 - j] = arr[n - 1 - j][i];
				arr[n - 1 - j][i] = arr[i][j];
				arr[i][j] = t;
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				arr[i][j] += i + n - j;
			}
		}
	}
	
	public void plane() {
		int n = arr.length;
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				arr[i][j] -= i + n - j;
			}
		}
		
		for (int i = 0; i < n / 2; i++) {
			for (int j = 0; j < n / 2; j++) {
				char t = arr[j][n - 1 -i];
				arr[j][n - 1 -i] = arr[n - 1 - i][n - 1 - j];
				arr[n - 1 - i][n - 1 - j] = arr[n - 1 - j][i];
				arr[n - 1 - j][i] = arr[i][j];
				arr[i][j] = t;
			}
		}
		for (int i = 0; i < n / 2; i++) {
			for (int j = 0; j < n / 2; j++) {
				char t = arr[j][n - 1 -i];
				arr[j][n - 1 -i] = arr[n - 1 - i][n - 1 - j];
				arr[n - 1 - i][n - 1 - j] = arr[n - 1 - j][i];
				arr[n - 1 - j][i] = arr[i][j];
				arr[i][j] = t;
			}
		}

		for (int i = 0; i < n / 2; i++) {
			for (int j = 0; j < n / 2; j++) {
				char t = arr[j][n - 1 -i];
				arr[j][n - 1 -i] = arr[n - 1 - i][n - 1 - j];
				arr[n - 1 - i][n - 1 - j] = arr[n - 1 - j][i];
				arr[n - 1 - j][i] = arr[i][j];
				arr[i][j] = t;
			}
		}
		/*
		// Debugger 
		for (int row = 0; row < arr.length; row++) {
			for (int col = 0; col < arr[row].length; col++) {
				System.out.printf("%5c", arr[row][col]);
			}
			System.out.println();
		}
		System.out.println();
		*/
	}
	
	public void space(int n) {
		arr[(35 - n) / 6][(35 - n) % 6] += (n / 6) + (n % 6);
		if (n != 0) {
			n--;
			space(n);
		}
	}

	public void space_old(int n) {
		arr[(35 - n) / 6][(35 - n) % 6] -= (n / 6) + (n % 6);
		if (n != 0) {
			n--;
			space_old(n);
		}
	}
	
	
	public void time_old() {
		int[][] t = {{8, 65, -18, -21, -15, 55}, 
				{8, 48, 57, 63, -13, 5}, 
				{16, -5, -26, 54, -7, -2}, 
				{48, 49, 65, 57, 2, 10}, 
				{9, -2, -1, -9, -11, -10}, 
				{56, 53, 18, 42, -28, 5}};
		for (int j = 0; j < arr[0].length; j++)
			for (int i = 0; i < arr.length; i++)
				arr[i][j] += t[j][i];
	}
	public void time() {
		int[][] t = {{8, 65, -18, -21, -15, 55}, 
				{8, 48, 57, 63, -13, 5}, 
				{16, -5, -26, 54, -7, -2}, 
				{48, 49, 65, 57, 2, 10}, 
				{9, -2, -1, -9, -11, -10}, 
				{56, 53, 18, 42, -28, 5}};
		for (int j = 0; j < arr[0].length; j++)
			for (int i = 0; i < arr.length; i++)
				arr[i][j] -= t[j][i];
		/*
		for (int row = 0; row < arr.length; row++) {
			for (int col = 0; col < arr[row].length; col++) {
				System.out.printf("%5c", arr[row][col]);
			}
			System.out.println();
		}
		System.out.println();
		*/
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the flag: ");
		String s = in.next();
		if (s.length() == 36) {
			Multidimensional f = new Multidimensional(s);
			f.time();
			f.space(35);
			f.plane();
			f.line();
			
			
			for (int row = 0; row < f.arr.length; row++) {
				for (int col = 0; col < f.arr[row].length; col++) {
					System.out.printf("%5c", f.arr[row][col]);
				}
				System.out.println();
			}
			System.out.println();
			
			if (f.check())
				System.out.println("Congratulations! You have transcended beyond dimensions");
			else
				System.out.println("Hmm, that's not correct2");
		} else {
			System.out.println("Hmm, that's not correct1.");
		}
		in.close();
	}

}
