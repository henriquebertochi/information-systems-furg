// Classes Abstratas e Polimorfismo

abstract class Shape {
    private String shapeName;

    public Shape(String shapeName) {
        this.shapeName = shapeName;
    }

    public abstract double area();

    @Override
    public String toString() {
        return "Forma: " + shapeName;
    }
}

class Sphere extends Shape {
    private double radius;

    public Sphere(double radius) {
        super("Esfera");
        this.radius = radius;
    }

    @Override
    public double area() {
        return 4 * Math.PI * radius * radius;
    }

    @Override
    public String toString() {
        return super.toString() + ", Raio: " + radius;
    }
}

class RectangularPrism extends Shape {
    private double height, width, length;

    public RectangularPrism(double height, double width, double length) {
        super("Prisma Retangular");
        this.height = height;
        this.width = width;
        this.length = length;
    }

    @Override
    public double area() {
        return 2 * (height * width + height * length + width * length);
    }

    @Override
    public String toString() {
        return super.toString() + ", Altura: " + height + ", Largura: " + width + ", Comprimento: " + length;
    }
}

class Cylinder extends Shape {
    private double radius, height;

    public Cylinder(double radius, double height) {
        super("Cilindro");
        this.radius = radius;
        this.height = height;
    }

    @Override
    public double area() {
        return 2 * Math.PI * radius * radius + 2 * Math.PI * radius * height;
    }

    @Override
    public String toString() {
        return super.toString() + ", Raio: " + radius + ", Altura: " + height;
    }
}

public class Paint {
    private double coverage; // Número de cm² por galão/latão

    public Paint(double coverage) {
        this.coverage = coverage;
    }

    public double amount(Shape s) {
        return s.area() / coverage;
    }
}

import java.text.DecimalFormat;

public class PaintThings {
    public static void main(String[] args) {
        final double COVERAGE = 350; // Cobertura em cm² por galão
        Paint paint = new Paint(COVERAGE);

        // Instanciar formas
        RectangularPrism deck = new RectangularPrism(20, 35, 10);
        Sphere bigBall = new Sphere(15);
        Cylinder tank = new Cylinder(10, 30);

        // Computar a quantidade de tinta necessária
        double deckAmt = paint.amount(deck);
        double ballAmt = paint.amount(bigBall);
        double tankAmt = paint.amount(tank);

        // Mostrar a quantidade de tinta necessária
        DecimalFormat fmt = new DecimalFormat("0.#");
        System.out.println("\n# de latões necessários...");
        System.out.println("Deck: " + fmt.format(deckAmt));
        System.out.println("Big Ball: " + fmt.format(ballAmt));
        System.out.println("Tank: " + fmt.format(tankAmt));
    }
}