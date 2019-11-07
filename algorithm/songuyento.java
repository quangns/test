/**
 * Tinh tich cua A so nguyen to lien nhau be hon mot so B cho truoc
 * 
 * Input:
 * - So a cho truoc la 4096
 * - Can tinh tich cua 3 so nguyen to sao cho tich 3 so nguyen to do be hon so a
 * 
 * Output:
 * - Tich cua 3 so nguyen to
 * 
 */

import java.util.ArrayList;
import java.util.List;

public class Main {
	//	Tao ra 1 mang chua cac so nguyen to
	private static List<Integer> num_prime = new ArrayList<Integer>();
	
    /*	Kiem tra xem so do co phai la so nguyen to khong
	neu la so nguyen to thi them vao mang num_prime */
	private boolean checkprime(int x) {
		for(int i = 0; i < num_prime.size(); i++) {
			if (x % num_prime.get(i) == 0) {
				return false;
			}
		}
		num_prime.add(x);
		return true;
	}
	
	public static void main(String[] args) {
		double pre_number = 4096;
		int soluong = 3;
		int tich = 1;
		num_prime.add(2);
		Main bai = new Main();
		for (int i = 3; i < pre_number/2; i+=2) {
			bai.checkprime(i);
			if (num_prime.size() > soluong) {
				int sp = num_prime.size()-1;
				int tmp =1;
				for (int k = 0; k< soluong; k++)
					tmp *= num_prime.get(sp-k);
				if(tmp > tich && tmp < pre_number)
                    tich = tmp;
				else if (tmp > pre_number)
					break;
			}
		}
		System.out.println(num_prime);
		System.out.println(tich);
	}
}
