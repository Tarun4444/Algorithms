// C++ program to rotate a matrix by 90 degrees
import java.io.*;
import java.util.scanner;

// An Inplace function to rotate a N x N matrix
// by 90 degrees in anti-clockwise direction
public class HelloWorld {
	public static void rotateMatrix(int mat[n][n])
	{
		// Consider all squares one by one
		for (int x = 0; x < n / 2; x++)
		{
				for (int y = x; y < n-x-1; y++)
					{
							int temp = mat[x][y];

							// move values from left to top
							mat[x][y] = mat[n-1-y][x];

							// move values from bottom to left
							mat[n-1-y][x] = mat[n-1-x][n-1-y];

							// move values from right to bottom
							mat[n-1-x][n-1-y] = mat[y][n-1-x];

							// assign temp to left
							mat[y][n-1-x] = temp;
			}
		}
	}

	// Function to print the matrix
	public static void displayMatrix(int mat[n][n])
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
				System.out.println(mat[i][j]);

			System.out.println();
		}
		System.out.println();
	}

	public static void main(String[] args)throws IOException {
		Scanner sc=new Scanner(System.in);
		    int n=sc.nextInt();
		    int mat[][]=new int[n][n];
			for(int i=0;i<n;i++){
			    for(int j=0;j<n;j++){
			        mat[i][j]=sc.nextInt();
			    }
			}
			rotateMatrix(mat);
			displayMatrix(mat);
		}
	}
}
