
public class AccountingApp {

	public static void main(String[] args) {
		
		System.out.println("���� : " + 10000 + "��");
		System.out.println("VAT : " + 10000 * 0.1 + "��");
		System.out.println("�ǸŰ� : " + (10000 + 10000 * 0.1) + "��");
		System.out.println("��� : " + 10000 * 0.3 + "��");
		System.out.println("���� : " + (10000 - 10000 * 0.3) + "��");
		System.out.println("���1 : " + (10000 - 10000 * 0.3) * 0.5 + "��");
		System.out.println("���2 : " + (10000 - 10000 * 0.3) * 0.3 + "��");
		System.out.println("���3 : " + (10000 - 10000 * 0.3) * 0.2 + "��");
		System.out.printf("%012d�� %012.4f", 3512312, 42.31531);

	}

}
