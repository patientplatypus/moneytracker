package vuespringexample.vuespring;

import org.springframework.boot.SpringApplication;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.Configuration;



@Configuration
@EnableAutoConfiguration
@EntityScan("vuespringexample.vuespring.models")
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}
}
