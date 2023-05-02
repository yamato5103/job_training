package object_d;

public class Wizard {
	String name;
	int hp;
	public void heal(Hero h) {
		h.hp+=10;
		System.out.println(h.name+"recoverd 10");
		
	}

}
