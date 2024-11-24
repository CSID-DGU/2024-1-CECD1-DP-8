package com.cecd.dp.domain.meta.repository;

import com.cecd.dp.domain.influencer.dto.FollowerChartProjection;
import com.cecd.dp.domain.meta.entity.Meta;
import java.util.List;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

public interface MetaRepository extends JpaRepository<Meta, Long> {

  @Query("SELECT m " + "FROM Meta m " + "WHERE m.influencer.id = :id")
  List<Meta> findMetaByInfluencerId(@Param("id") Long influencerId, Pageable pageable);

  @Query(
      "SELECT m.followerCnt AS followerCnt, m.createdAt AS createdAt "
          + "FROM Meta AS m "
          + "WHERE m.influencer.id = :influencerId "
          + "ORDER BY m.createdAt ASC")
  List<FollowerChartProjection> findFollowerChartById(Long influencerId);
}
