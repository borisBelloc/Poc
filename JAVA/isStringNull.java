public class MyStringUtils {

  // check if a string is null
	public static boolean isNullOrEmpty(String stringToTest) {
		return stringToTest == null || stringToTest.trim().isEmpty();
	}

}
