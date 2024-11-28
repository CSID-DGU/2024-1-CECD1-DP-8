package com.cecd.dp.domain.influencer.entity;

import com.cecd.dp.domain.media.entity.Media;
import com.cecd.dp.domain.meta.entity.Meta;
import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@AllArgsConstructor
@Getter
public class Influencer {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  @Column(name = "influencer_id")
  private Long id;

  // GRAPH 조회 owner ID
  private String graphId;

  // 인스타 별명
  @Column(unique = true)
  private String nickname;

  // 인스타 이름
  private String name;

  // 카테고리(ex. 사진가... etc)
  private String category;

  // 소개
  private String biography;

  // 프로필 사진
  @Column(length = 300)
  private String profilePictureUrl;

  // 웹사이트 링크
  private String website;

  @OneToMany(mappedBy = "influencer", cascade = CascadeType.ALL)
  List<Media> mediaList = new ArrayList<>();

  @OneToMany(mappedBy = "influencer", cascade = CascadeType.ALL)
  List<Meta> metaList = new ArrayList<>();

  // ===연관관계 편의 메서드===//
  public void addMedia(Media media) {
    if (mediaList.contains(media)) {
      mediaList.remove(media);
    }
    media.setInfluencer(this);
    this.mediaList.add(media);
  }

  public void addMeta(Meta meta) {
    if (metaList.contains(meta)) {
      metaList.remove(meta);
    }
    meta.setInfluencer(this);
    this.metaList.add(meta);
  }

  // ===보조 메서드===//
  public Meta getLatestMeta() {
    return metaList.get(metaList.size() - 1);
  }

  public Integer getMediaCnt() {
    return this.mediaList.stream()
        .sorted(Comparator.comparing(Media::getPostedAt).reversed())
        .limit(50)
        .filter(m -> m.getMediaProductType().equals("FEED"))
        .toList()
        .size();
  }

  public Integer getReelsMediaCnt() {
    return this.mediaList.stream()
        .sorted(Comparator.comparing(Media::getPostedAt).reversed())
        .limit(50)
        .filter(m -> m.getMediaProductType().equals("REELS"))
        .toList()
        .size();
  }

  public Integer getAdMediaCnt() {
    return this.mediaList.stream()
        .sorted(Comparator.comparing(Media::getPostedAt).reversed())
        .limit(50)
        .filter(Media::getIsAd)
        .toList()
        .size();
  }

  public Integer getNonAdMediaCnt() {
    return this.mediaList.stream()
        .sorted(Comparator.comparing(Media::getPostedAt).reversed())
        .limit(50)
        .filter(m -> !m.getIsAd())
        .toList()
        .size();
  }

  public Double getLikeAvgOfAdMediaWithOutHide() {
    return this.mediaList.stream()
        .sorted(Comparator.comparing(Media::getPostedAt).reversed())
        .limit(50)
        .filter(Media::getIsAd) // 광고 게시물만 필터링
        .filter(m -> m.getLikeCnt() > 0) // 좋아요 숨기기한 게시물 제외 (isLikeHidden을 예로 가정)
        .mapToDouble(Media::getLikeCnt) // 좋아요 수를 IntStream으로 변환
        .average() // 평균을 구함
        .orElse(0.0); // 만약 결과가 없으면 0을 반환
  }

  public Double getLikeAvgOfAdMedia() {
    return this.mediaList.stream()
        .sorted(Comparator.comparing(Media::getPostedAt).reversed())
        .limit(50)
        .filter(Media::getIsAd)
        .mapToDouble(Media::getCommentsCnt)
        .average()
        .orElse(0.0);
  }
}
