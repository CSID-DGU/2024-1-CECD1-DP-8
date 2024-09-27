package com.cecd.dp.domain.media.repository;

import com.cecd.dp.domain.media.entity.Media;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

public interface MediaRepository extends JpaRepository<Media, Long> {

  @Query(
      "SELECT "
          + "CASE WHEN COUNT(m) = 0 THEN 0.0 "
          + "ELSE CAST(COUNT(CASE WHEN m.isAd = true THEN 1 END) AS float) / COUNT(m) END "
          + "FROM Media m "
          + "WHERE m.influencer.id = :id")
  Float calculateAdMediaPercentageByInfluencerId(@Param("id") Long influencerId);

  @Query(
      "SELECT SUM(CASE WHEN m.mediaProductType = 'REELS' THEN 1 ELSE 0 END) / CAST(COUNT(*) AS FLOAT) AS reels_ratio "
          + "FROM Media m "
          + "WHERE m.influencer.id = :id")
  Float calculateReelsMediaPercentageByInfluencerId(@Param("id") Long influencerId);
}
