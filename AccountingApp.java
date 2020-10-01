
public class AccountingApp {

	public static void main(String[] args) {
		
		System.out.println("원가 : " + 10000 + "원");
		System.out.println("VAT : " + 10000 * 0.1 + "원");
		System.out.println("판매가 : " + (10000 + 10000 * 0.1) + "원");
		System.out.println("비용 : " + 10000 * 0.3 + "원");
		System.out.println("이익 : " + (10000 - 10000 * 0.3) + "원");
		System.out.println("사람1 : " + (10000 - 10000 * 0.3) * 0.5 + "원");
		System.out.println("사람2 : " + (10000 - 10000 * 0.3) * 0.3 + "원");
		System.out.println("사람3 : " + (10000 - 10000 * 0.3) * 0.2 + "원");
		System.out.printf("%012d와 %012.4f", 3512312, 42.31531);

	}

}
