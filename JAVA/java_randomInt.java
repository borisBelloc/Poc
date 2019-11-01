import java.util.Random;


public class RandomUtil {
	
	
	/**
	 * Generates a random integer from 0 (inclusive) to vMax (inclusive)
	 * @param vMax
	 * @return int
	 */
	public static int getRandomInt(int vMax ) {
		return new Random().nextInt(vMax +1);
	}
	
	/**
	 * Generates a random integer between vMin (inclusive) and vMax (inclusive).
	 * @param vMin
	 * @param vMax
	 * @return int
	 */
	public static int getRandomIntInRange(int vMin, int vMax) {
		if (vMin >= vMax) {
			throw new IllegalArgumentException("max must be greater than min");
		}
		return new Random().nextInt((vMax) + 1) + vMin;
	}
	
	
	
	/** ------------------------------
	* Test; not finished ;
	*/
	private void getRandomInt() {
		// sauce: https://stackoverflow.com/a/363692/9552861

    	// TODO: Change min and max to desired values
		int randomNum = ThreadLocalRandom.current().nextInt(min, max + 1);
		System.out.println(randomNum);
	}
}
