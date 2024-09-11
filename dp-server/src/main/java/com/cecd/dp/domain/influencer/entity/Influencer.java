package com.cecd.dp.domain.influencer.entity;

import com.cecd.dp.domain.media.entity.Media;
import com.cecd.dp.domain.meta.entity.Meta;
import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;

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
  private String nickname;

  // 인스타 이름
  private String name;

  // 카테고리(ex. 사진가... etc)
  private String category;

  // 소개
  private String biography;

  // 프로필 사진
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
    return mediaList.size();
  }
}
