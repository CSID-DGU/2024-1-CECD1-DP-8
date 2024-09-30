package com.cecd.dp.domain.media.repository;

import com.cecd.dp.domain.media.dto.MediaChartProjection;
import com.cecd.dp.domain.media.entity.Media;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

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

  @Query(value =
          "SELECT " +
                  "    SUM(CASE WHEN m.like_cnt = -1 THEN 0 ELSE m.like_cnt END) AS total_cnt, " +
                  "    CAST(m.posted_at AS DATE) " +
                  "FROM " +
                  "    (SELECT gs.posted_at " +
                  "     FROM generate_series( " +
                  "        (SELECT MIN(posted_at) FROM media), " +
                  "        NOW(), " +
                  "        INTERVAL '7 days' " +
                  "     ) AS gs(posted_at)) AS gs " +
                  "LEFT JOIN media m ON CAST(m.posted_at AS DATE) < CAST(gs.posted_at AS DATE) + INTERVAL '7 days' " +
                  "    AND CAST(m.posted_at AS DATE) >= CAST(gs.posted_at AS DATE) " +
                  "WHERE " +
                  "    m.influencer_id = :id AND m.media_product_type = 'REELS' " +
                  "GROUP BY " +
                  "    CAST(m.posted_at AS DATE)" +
                  "ORDER BY " +
                  "    CAST(m.posted_at AS DATE) ASC",
          nativeQuery = true)
  List<MediaChartProjection> getReelsChartLikesByWeek(@Param("id") Long influencerId);

  @Query( value =
          "SELECT SUM(CASE WHEN m.like_cnt = -1 THEN 0 ELSE m.like_cnt END) AS total_cnt, "
          + "CAST(m.posted_at AS DATE) "
          + "FROM media m "
          + "WHERE m.influencer_id = :id AND m.media_product_type = 'REELS' "
          + "GROUP BY CAST(m.posted_at AS DATE) "
          + "ORDER BY CAST(m.posted_at AS DATE) ASC"
  , nativeQuery = true)
  List<MediaChartProjection> getReelsChartLikesByDay(@Param("id") Long influencerId);


  @Query(value =
          "SELECT " +
                  "    SUM(CASE WHEN m.comments_cnt = -1 THEN 0 ELSE m.comments_cnt END) AS total_cnt, " +
                  "    CAST(m.posted_at AS DATE) " +
                  "FROM " +
                  "    (SELECT gs.posted_at " +
                  "     FROM generate_series( " +
                  "        (SELECT MIN(posted_at) FROM media), " +
                  "        NOW(), " +
                  "        INTERVAL '7 days' " +
                  "     ) AS gs(posted_at)) AS gs " +
                  "LEFT JOIN media m ON CAST(m.posted_at AS DATE) < CAST(gs.posted_at AS DATE) + INTERVAL '7 days' " +
                  "    AND CAST(m.posted_at AS DATE) >= CAST(gs.posted_at AS DATE) " +
                  "WHERE " +
                  "    m.influencer_id = :id AND m.media_product_type = 'REELS' " +
                  "GROUP BY " +
                  "    CAST(m.posted_at AS DATE)" +
                  "ORDER BY " +
                  "    CAST(m.posted_at AS DATE) ASC",
          nativeQuery = true)
  List<MediaChartProjection> getReelsChartCommentsByWeek(@Param("id") Long influencerId);

  @Query( value =
          "SELECT SUM(CASE WHEN m.comments_cnt = -1 THEN 0 ELSE m.comments_cnt END) AS total_cnt, "
                  + "CAST(m.posted_at AS DATE) "
                  + "FROM media m "
                  + "WHERE m.influencer_id = :id AND m.media_product_type = 'REELS' "
                  + "GROUP BY CAST(m.posted_at AS DATE) "
                  + "ORDER BY CAST(m.posted_at AS DATE) ASC"
          , nativeQuery = true)
  List<MediaChartProjection> getReelsChartCommentsByDay(@Param("id") Long influencerId);

}
