package object_dir;

public class Hero {

	String name;
	int hp;

	public void sleep() {
		this.hp = 100;
		System.out.println(this.name + "は眠って回復した");
	}

	public void sit(int sec) {
		this.hp += sec;
		System.out.println(this.name + "は" + sec + "秒座った");
		System.out.println("HP" + sec + "recoverded");
	}

	public void slip() {
		this.hp = 5;
		System.out.println(this.name + "is slip!");
		System.out.println("5 damage");

	}

	public void run() {
		System.out.println(this.name);
		System.out.println("GAME OVER");
		System.out.println("final HP is" + this.hp);
	}

}
