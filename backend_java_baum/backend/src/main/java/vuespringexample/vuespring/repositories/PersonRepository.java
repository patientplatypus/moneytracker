package vuespringexample.vuespring.repositories;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import vuespringexample.vuespring.models.Person;

public interface PersonRepository extends AbstractRepository<Person, Long> {

}
