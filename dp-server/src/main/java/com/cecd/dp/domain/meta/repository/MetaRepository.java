package com.cecd.dp.domain.meta.repository;

import com.cecd.dp.domain.meta.entity.Meta;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface MetaRepository extends JpaRepository<Meta, Long> {

    @Query(
            "SELECT m "
            + "FROM Meta m "
            + "WHERE m.influencer.id = :id"
    )
    List<Meta> findMetaByInfluencerId(@Param("id") Long influencerId, Pageable pageable);
}
