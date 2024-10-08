package com.cecd.dp.domain.influencer.repository;

import com.cecd.dp.domain.influencer.dto.MostPostsProjection;
import com.cecd.dp.domain.influencer.dto.ProfileProjection;
import com.cecd.dp.domain.influencer.entity.Influencer;
import java.util.List;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

public interface InfluencerRepository extends JpaRepository<Influencer, Long> {

  @Query(
      "SELECT new com.cecd.dp.domain.influencer.dto.ProfileProjection(i.profilePictureUrl, i.nickname, i.name, i.category, SIZE(md), mt.followerCnt) "
          + "FROM Influencer i "
          + "JOIN i.mediaList md "
          + "JOIN i.metaList mt "
          + "WHERE i.id = :id "
          + "ORDER BY mt.createdAt DESC")
  List<ProfileProjection> getProfileById(@Param("id") Long influencerId, Pageable pageable);

  @Query(
      "SELECT new com.cecd.dp.domain.influencer.dto.MostPostsProjection(md.uniqueCode) "
          + "FROM Influencer i JOIN i.mediaList md "
          + "WHERE i.id = :id "
          + "ORDER BY (md.likeCnt + md.commentsCnt) DESC")
  List<MostPostsProjection> getMostThreePostsCodesById(
      @Param("id") Long influencerId, Pageable pageable);

  @Query(
      "SELECT DISTINCT ht.name "
          + "FROM Influencer i "
          + "JOIN i.mediaList md "
          + "JOIN md.mediaHashTagList mht "
          + "JOIN mht.hashTag ht "
          + "WHERE i.id = :id")
  List<String> getAllTagNamesById(@Param("id") Long influencerId);

  @Query(
      "SELECT (mt.likeAvg+mt.commentsAvg)/mt.followerCnt*100 "
          + "FROM Influencer i JOIN i.metaList mt "
          + "WHERE i.id = :id "
          + "ORDER BY mt.createdAt DESC")
  List<Float> calculateReactionQuotientById(@Param("id") Long influencerId, Pageable pageable);

  @Query(
      value =
          "SELECT AVG(subquery.like_cnt) "
              + "FROM ( "
              + "    SELECT m.like_cnt "
              + "    FROM Media m "
              + "    WHERE m.influencer_id = :id "
              + "    ORDER BY m.created_at DESC "
              + "    LIMIT 7 "
              + ") AS subquery",
      nativeQuery = true)
  Float getCurrentWeekLikeAvgById(@Param("id") Long influencerId);

  @Query(
      value =
          "SELECT AVG(subquery.comments_cnt) "
              + "FROM ( "
              + "    SELECT m.comments_cnt "
              + "    FROM Media m "
              + "    WHERE m.influencer_id = :id "
              + "    ORDER BY m.created_at DESC "
              + "    LIMIT 7 "
              + ") AS subquery",
      nativeQuery = true)
  Float getCurrentWeekCommentsAvgById(@Param("id") Long influencerId);
}
