package object_d;

public class Hero {

	String name;
	int hp;
	Sword sword;

	public void attack(Matango m) {
		System.out.println(this.name);
		m.hp-=5;
		System.out.println("enemy 5damage");
	}

	//over_road_hero_class
	//	class with arguments
	public Hero(String name) {
		this.hp = 100;
		this.name = name;
	}

	public Hero() {
		this("dummy");
		
	}

	public void sleep() {
		this.hp = 100;
		System.out.println(this.name + "は眠って回復した");
	}

	public void sit(int sec) {
		this.hp += sec;
		System.out.println(this.name + "は" + sec + "秒座った");
		System.out.println("hp" + sec + "recoverded");
	}

	public void slip() {
		this.hp = 5;
		System.out.println(this.name + "is slip!");
		System.out.println("5 damage");

	}

	public void run() {
		System.out.println(this.name);
		
	}

}
