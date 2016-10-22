public class Main {

    public static void main(String[] args) {
        int x = 0b1001;
        System.out.printf("%d\n", x);
        boolean learnedHTML = true;
        boolean learnedJavaScript = true;
        boolean learnedCSS = false;
        boolean isQualified = (
                learnedHTML &&
                        learnedJavaScript &&
                        learnedCSS
        );
        System.out.printf("Carlos is qualified :[%b]\n", isQualified);

        int myCounter = 0;
        do {
            myCounter += 1;
            System.out.printf("Current counter is %d\n", myCounter);
        } while (myCounter < 5);

        String longSentence = "This is a long fucking sentence !";
        String desiredWord = "FUCKING";

        if (longSentence.toLowerCase().contains(desiredWord.toLowerCase())) // Can be used instead of equalsIgnoreCase
            System.out.println("Yep it is inside !");
        else
            System.out.println("Nope it is not!");
        int dollarsToString = Integer.parseInt("-5"); //casting
        System.out.printf("dollars are %d\n", dollarsToString);
        // boolean algebra
        boolean greatExampleOr = false || false || false || true;
        boolean greatExampleAnd = false && false;

        System.out.printf("F || F || F || T = %b\n", greatExampleOr);
        System.out.printf("F && T = %b\n", greatExampleAnd);

        // PEZ
        System.out.println("We are making a new Pez dispenser");
        PezDispenser dispenser = new PezDispenser("Sponge Bob");
        System.out.printf("This dispenser character is %s\n", dispenser.getCharacterName());

        System.out.println("We are making a new Kart");
        GoKart kart = new GoKart("blue");
        System.out.printf("This kart is coloured - %s\n", kart.getColor());


        Bottle potion = new Bottle(Bottle.LiquidColor.GREEN,100);
        System.out.println(potion);

        Bottle potionOfHealing = new Bottle(Bottle.LiquidColor.BLACK, 100);
        System.out.println(potionOfHealing);

        System.out.println(potion.mixBottles(potionOfHealing).name());
        // state & behaviour


    } // END OF MAIN FUNCTION
} // END OF CLASS




/*
Not working in IDE , re-do with scan or something else !
import java.io.Console;

public class TreeStory {

    public static void main(String[] args) {
        Console console = System.console();
        String ageAsString = console.readLine("Your age?");
        int age = Integer.parseInt(ageAsString);
        if (age < 13 )

        {
          // exit code
          console.printf("You must be 13 to use this program ! ");
          System.exit(0);

        }

        /*  Some terms:
            noun - Person, place or thing
            verb - An action
            adjective - A description used to modify or describe a noun
            Enter your amazing code here
        */
/*
String name = console.readLine("Name:  ");
    String adjective  = console.readLine("Adjective: ");
    String noun ;
    boolean isInvalidWord;

      do {
              noun  = console.readLine("Noun: ");
              isInvalidWord = (noun.equalsIgnoreCase("gandon") ||
                               noun.equalsIgnoreCase("ueban") ||
                               noun.equalsIgnoreCase("invalid"));

              if (isInvalidWord)
              {
              console.printf("SAM GANDON!\n Try again  !\n");
              }


              } while (isInvalidWord);


              String adverb = console.readLine("Adverb: ");
              String verb = console.readLine("Verb: ");
              console.printf("%s is a %s %s \n",name,adjective,noun);
              console.printf("They are %s %s !\n",adverb, verb);

              }

              }
 */