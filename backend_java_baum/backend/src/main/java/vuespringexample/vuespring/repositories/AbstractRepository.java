package vuespringexample.vuespring.repositories;

import java.io.Serializable;
import java.util.List;
import org.springframework.data.repository.NoRepositoryBean;
import org.springframework.data.repository.Repository;

/**
 * Common base repository for all other repositories.
 */
@NoRepositoryBean
public interface AbstractRepository<T, ID extends Serializable> extends Repository<T, ID> {

    /**
     * Deletes an entity.
     */
    void delete(T entity);

    /**
     * Returns all instances of the type.
     */
    List<T> findAll();

    /**
     * Retrieves an entity by its id.
     */
    T findOne(ID id);

    /**
     * Saves a given entity.
     */
    <S extends T> S save(S entity);
}

