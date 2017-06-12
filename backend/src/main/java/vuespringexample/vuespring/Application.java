
package hello;

import org.springframework.boot.SpringApplication;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.boot.autoconfigure.SpringBootApplication;


@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}
}
