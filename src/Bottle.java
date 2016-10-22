/**
 * Created by miross1 on 10/20/2016.
 */

public class Bottle {

    public enum LiquidColor {
        RED , GREEN , BLUE ,
        ARGENT, BLACK, AZURE,
        PURPLE;

        private LiquidColor mixedColor(LiquidColor liquidColor){
            return LiquidColor.values()[(int) (Math.random()*LiquidColor.values().length)];
        }

    }

    private LiquidColor bottleColor;
    private int fillPercentage;


    // Default constructor
    // This way user will have al options
    public Bottle() {
        bottleColor = null;
        fillPercentage = 0;
    }

    public Bottle(LiquidColor bottleColor, int fillPercentage) {
        this();
        this.bottleColor = bottleColor;
        this.fillPercentage = fillPercentage;
    }

    public Bottle(LiquidColor bottleColor) {
        this();
        this.bottleColor = bottleColor;
    }

    public Bottle(int fillPercentage) {
        this();
        this.fillPercentage = fillPercentage;
    }

    @Override
    public String toString() {
        return getClass().getSimpleName()+"{" +
                "The color is ='" + bottleColor.name() + '\'' +
                " " + fillPercentage + "% full" +
                '}';
    }

    public LiquidColor getBottleColor() {
        return bottleColor;
    }

    public int getFillPercentage() {
        return fillPercentage;
    }

    public void setBottleColor(LiquidColor bottleColor) {
        this.bottleColor = bottleColor;
    }

    public void setFillPercentage(int fillPercentage) {
        this.fillPercentage = fillPercentage;
    }
    public LiquidColor mixBottles(Bottle bottle){
        return bottleColor.mixedColor(bottle.getBottleColor());
    }
}