// Aplicação de Formas Geométricas com Herança

abstract class Shape {
    protected String color;
    protected boolean filled;

    public Shape(String color, boolean filled) {
        this.color = color;
        this.filled = filled;
    }

    public void setFilled(boolean filled) {
        this.filled = filled;
    }

    public abstract double area();

    @Override
    public String toString() {
        return "Cor: " + color + ", Preenchido: " + filled;
    }
}

class Circle extends Shape {
    private double radius;

    public Circle(double radius, String color, boolean filled) {
        super(color, filled);
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }

    @Override
    public String toString() {
        return "Círculo - " + super.toString() + ", Raio: " + radius;
    }
}

class Square extends Shape {
    private double side;

    public Square(double side, String color, boolean filled) {
        super(color, filled);
        this.side = side;
    }

    @Override
    public double area() {
        return side * side;
    }

    @Override
    public String toString() {
        return "Quadrado - " + super.toString() + ", Lado: " + side;
    }
}

class Rectangle extends Shape {
    private double width, height;

    public Rectangle(double width, double height, String color, boolean filled) {
        super(color, filled);
        this.width = width;
        this.height = height;
    }

    @Override
    public double area() {
        return width * height;
    }

    @Override
    public String toString() {
        return "Retângulo - " + super.toString() + ", Largura: " + width + ", Altura: " + height;
    }
}

public class Main {
    public static void main(String[] args) {
        Circle circle = new Circle(7, "Azul", true);
        Square square = new Square(5, "Sem cor", false);
        Rectangle rectangle = new Rectangle(3, 6, "Preto", true);
        Shape shape = new Shape("Verde", true) {
            @Override
            public double area() {
                return 0;
            }
        };

        rectangle.setFilled(false);
        showInfo(circle);
        showInfo(square);
        showInfo(rectangle);
        showInfo(shape);
    }

    public static void showInfo(Shape shape) {
        System.out.println("Informações da forma:");
        System.out.println(shape.toString());
    }
}