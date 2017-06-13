package vuespringexample.vuespring.controllers;

import vuespringexample.vuespring.models.Person;
import vuespringexample.vuespring.repositories.PersonRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Collection;
import java.util.List;


@RestController
@RequestMapping("/person")
public class PersonController {

        @Autowired
        private PersonRepository repository;

        @RequestMapping(method = RequestMethod.GET)
        public ResponseEntity<Collection<Person>> getAllPersons(){
            return new ResponseEntity<>((Collection<Person>) repository.findAll(), HttpStatus.OK);
        }

        @RequestMapping(method = RequestMethod.GET, value = "/{id}")
        public ResponseEntity<Person> getPersonWithId(@PathVariable Long id) {
            return new ResponseEntity<>(repository.findOne(id),HttpStatus.OK);
        }

        // @RequestMapping(method = RequestMethod.GET, params = {"name"})
        // public ResponseEntity<Collection<Person>> findPersonWithName(@RequestParam(value="firstname") String firstname) {
        //     return new ResponseEntity<>(repository.findByName(firstname), HttpStatus.OK);
        // }

        @RequestMapping(method = RequestMethod.POST)
        public ResponseEntity<?> addPerson(@RequestBody Person input) {
            return new ResponseEntity<>(repository.save(input), HttpStatus.CREATED);
        }
}
