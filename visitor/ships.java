class Ship {
    protected String name;

    public Ship() {
        this.name = "ship";
    }

    public void collide(Asteroid ast) {
        System.out.println(this.name + " collides asteroid");
    }

    public void collide(ExplodingAsteroid ast) {
        System.out.println(this.name + " collides exploding asteroid");
    }

    public void accept(Asteroid ast) {
         ast.visit(this);
    }

    public String getName() {
        return name;
    }

}

class ImperialShip extends Ship {
    public ImperialShip() {
        this.name = "imperial ship";
    }

}

class Asteroid {

    public void visit(Ship ship) {
        System.out.println(ship.getName() + " collides asteroid");
    }
}

class ExplodingAsteroid extends Asteroid {
    public void visit(Ship ship) {
        System.out.println(ship.getName() + " collides exploding asteroid");
    }

}


public class ships {
    public static void main(final String[] args) {
        Ship ship = new ImperialShip();
        Asteroid ast = new ExplodingAsteroid();
        ship.collide(ast); // imperial ship collides asteroid
        // ship.accept(ast);
        ship.accept(ast);
    }
}
