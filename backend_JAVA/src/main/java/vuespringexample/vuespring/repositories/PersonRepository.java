
package vuespringexample.vuespring.repositories;

import java.util.List;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.repository.query.Param;
import vuespringexample.vuespring.models.Person;

public interface PersonRepository extends MongoRepository<Person, String> {
		List<Person> findByName(String firstName);
	}
