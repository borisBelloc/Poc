import java.util.Scanner;

public class Utils {

	public static void main(String[] args) {
  // USE :
  int userChoice = Utils.isUserInputOk(1);
  }
	
    /**
     * Used to collect user's input and check if it's an int
     * @return user choice as int
     */
    public static int userInputInt() {
        Scanner sc = new Scanner(System.in);
        while (!sc.hasNextInt()) {
            String input = sc.next();
            System.out.printf("\"%s\" is not valid ! Please enter an integer number.\n", input);
        }
//        sc.close();
        return sc.nextInt();
    }

    /**
     * Check if the user input is in the allowed choice range
     *
     * @param origin     origin (allowed value):
     *                    1 : 1 <= x <= 3
     *                    2 : 1 <= x <= 4
     * @param userChoice : input entered by the user
     * @return boolean
     */
    public static boolean isUserRangeOk(int origin, int userChoice) {
        switch (origin) {
            case 1:
                if (userChoice > 0 && userChoice <= 3) {
                    return true;
                } else {
                	System.out.println("Your choice must be between 1 et 3");
                    return false;
                }
            case 2 : 
            	if (userChoice > 0 && userChoice <= 4) {
            		return true;
            	} else {
            		System.out.println("Your choice must be between 1 et 4");
            		return false;
            	}

        }
        return false;
    }
    
    /**
     * Waiting for correct user input
     * @return
     */
    public static int isUserInputOk(int origin) {
        int userChoice;
        do {
            System.out.println("Enter your choice : ");
        }
        while (!isUserRangeOk(origin, userChoice = userInputInt()));
        return userChoice;
    }
}
