package object_d;

public class SuperHero extends Hero {
	boolean flying;

	public void fly() {
		this.flying = true;
		System.out.println("Flied");
	}

	public void land() {
		this.flying = false;
		System.out.println("landing");
	}

	public void run() {
		System.out.println(this.name + " withdrawal");
	}

	public void attack(Matango m) {
		super.attack(m);
		if (this.flying) {
			super.attack(m);
		}
	}

}
