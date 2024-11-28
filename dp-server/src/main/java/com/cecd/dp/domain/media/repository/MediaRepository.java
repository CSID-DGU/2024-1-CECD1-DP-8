package com.cecd.dp.domain.media.repository;

import com.cecd.dp.domain.influencer.dto.HashTagInfoProjection;
import com.cecd.dp.domain.media.dto.MediaChartProjection;
import com.cecd.dp.domain.media.entity.Media;
import java.util.List;
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

  @Query(
      value =
          "SELECT "
              + "    SUM(CASE WHEN m.like_cnt = -1 THEN 0 ELSE m.like_cnt END) AS total_cnt, "
              + "    CAST(m.posted_at AS DATE) "
              + "FROM "
              + "    (SELECT gs.posted_at "
              + "     FROM generate_series( "
              + "        (SELECT MIN(posted_at) FROM media), "
              + "        NOW(), "
              + "        INTERVAL '7 days' "
              + "     ) AS gs(posted_at)) AS gs "
              + "LEFT JOIN media m ON CAST(m.posted_at AS DATE) < CAST(gs.posted_at AS DATE) + INTERVAL '7 days' "
              + "    AND CAST(m.posted_at AS DATE) >= CAST(gs.posted_at AS DATE) "
              + "WHERE "
              + "    m.influencer_id = :id AND m.media_product_type = 'REELS' "
              + "GROUP BY "
              + "    CAST(m.posted_at AS DATE)"
              + "ORDER BY "
              + "    CAST(m.posted_at AS DATE) ASC",
      nativeQuery = true)
  List<MediaChartProjection> getReelsChartLikesByWeek(@Param("id") Long influencerId);

  @Query(
      value =
          "SELECT SUM(CASE WHEN m.like_cnt = -1 THEN 0 ELSE m.like_cnt END) AS total_cnt, "
              + "CAST(m.posted_at AS DATE) "
              + "FROM media m "
              + "WHERE m.influencer_id = :id AND m.media_product_type = 'REELS' "
              + "GROUP BY CAST(m.posted_at AS DATE) "
              + "ORDER BY CAST(m.posted_at AS DATE) ASC",
      nativeQuery = true)
  List<MediaChartProjection> getReelsChartLikesByDay(@Param("id") Long influencerId);

  @Query(
      value =
          "SELECT "
              + "    SUM(CASE WHEN m.comments_cnt = -1 THEN 0 ELSE m.comments_cnt END) AS total_cnt, "
              + "    CAST(m.posted_at AS DATE) "
              + "FROM "
              + "    (SELECT gs.posted_at "
              + "     FROM generate_series( "
              + "        (SELECT MIN(posted_at) FROM media), "
              + "        NOW(), "
              + "        INTERVAL '7 days' "
              + "     ) AS gs(posted_at)) AS gs "
              + "LEFT JOIN media m ON CAST(m.posted_at AS DATE) < CAST(gs.posted_at AS DATE) + INTERVAL '7 days' "
              + "    AND CAST(m.posted_at AS DATE) >= CAST(gs.posted_at AS DATE) "
              + "WHERE "
              + "    m.influencer_id = :id AND m.media_product_type = 'REELS' "
              + "GROUP BY "
              + "    CAST(m.posted_at AS DATE)"
              + "ORDER BY "
              + "    CAST(m.posted_at AS DATE) ASC",
      nativeQuery = true)
  List<MediaChartProjection> getReelsChartCommentsByWeek(@Param("id") Long influencerId);

  @Query(
      value =
          "SELECT SUM(CASE WHEN m.comments_cnt = -1 THEN 0 ELSE m.comments_cnt END) AS total_cnt, "
              + "CAST(m.posted_at AS DATE) "
              + "FROM media m "
              + "WHERE m.influencer_id = :id AND m.media_product_type = 'REELS' "
              + "GROUP BY CAST(m.posted_at AS DATE) "
              + "ORDER BY CAST(m.posted_at AS DATE) ASC",
      nativeQuery = true)
  List<MediaChartProjection> getReelsChartCommentsByDay(@Param("id") Long influencerId);

  @Query(
      value =
          "with Recent50Media as ( "
              + "          select * from media "
              + "          where influencer_id = :influencerId "
              + "          order by posted_at desc "
              + "          limit 50), "
              + "  HashTagEngagement as ( "
              + "          SELECT "
              + "          m.media_id as media_id, "
              + "          m.influencer_id, "
              + "          m.like_cnt, "
              + "          m.comments_cnt, "
              + "          m.posted_at, "
              + "          hash_tag.name AS hash_tag_name, "
              + "          (m.like_cnt + m.comments_cnt) AS engagement_score "
              + "  FROM Recent50Media as m "
              + "  JOIN media_hash_tag ON m.media_id = media_hash_tag.media_id "
              + "  JOIN hash_tag ON media_hash_tag.hash_tag_id = hash_tag.hash_tag_id "
              + "  WHERE hash_tag.name NOT IN ('광고', '협찬', '제품제공', '제품협찬', '서포터즈', '유료광고', '대가성광고', '단순제공') "
              + "), "
              + "  HashTagState as( "
              + "          select "
              + "                  MAX(engagement_score) AS max_engagement, "
              + "  SUM(engagement_score) AS total_engagement, "
              + "  COUNT(*) AS usage_count, "
              + "  FLOOR(AVG(engagement_score)) AS avg_engagement, "
              + "          hash_tag_name "
              + "  from HashTagEngagement "
              + "  group by hash_tag_name "
              + ") "
              + "  select * "
              + "  from HashTagState "
              + "  order by usage_count desc limit 10 ",
      nativeQuery = true)
  List<HashTagInfoProjection> getHashTagReportByInfluencerId(
      @Param("influencerId") Long influencerId);
}
