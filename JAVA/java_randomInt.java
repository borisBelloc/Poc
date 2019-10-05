import java.util.concurrent.ThreadLocalRandom;

public class FigureUtil {
	
	private void getRandomInt() {
		// nextInt is normally exclusive of the top value,
		// so add 1 to make it inclusive
		// sauce: https://stackoverflow.com/a/363692/9552861

    // TODO: Change min and max to desired values
		int randomNum = ThreadLocalRandom.current().nextInt(min, max + 1);
		System.out.println(randomNum);
	}
}