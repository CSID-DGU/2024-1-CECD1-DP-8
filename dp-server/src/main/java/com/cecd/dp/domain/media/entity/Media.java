package com.cecd.dp.domain.media.entity;

import com.cecd.dp.domain.image.entity.Image;
import com.cecd.dp.domain.influencer.entity.Influencer;
import com.cecd.dp.domain.mediahashtag.entity.MediaHashTag;
import com.cecd.dp.global.BaseEntity;
import jakarta.persistence.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

import lombok.*;

@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@AllArgsConstructor
@Builder
public class Media extends BaseEntity {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  @Column(name = "media_id")
  //게시글 아이디
  private Long id;

  // Graph조회_미디어_아이디
  private String graphMediaId;

  // 댓글 수
  private Integer replyCnt;

  // 좋아요 수
  private Integer likeCnt;

  // 게시글 생성 유형(FEED||REELS)
  private String generatedType;

  // 게시글 유형(VIDEO|||CAROUSEL_ALBUM)
  private String postType;

  // 게시글 링크
  private String link;

  // 광고 글 여부
  private Boolean isAd;

  @Lob
  @Column(columnDefinition = "text")
  // 본문
  private String caption;

  // 썸네일 이미지(REELS일 경우에만 존재)
  private String thumbnailUrl;

  // media 작성 시간
  private LocalDateTime postedAt;

  @ManyToOne(fetch = FetchType.LAZY)
  @JoinColumn(name = "influencer_id")
  private Influencer influencer;

  @OneToMany(mappedBy = "media", cascade = CascadeType.ALL)
  private List<MediaHashTag> mediaHashTagList = new ArrayList<>();

  @OneToMany(mappedBy = "media", cascade = CascadeType.ALL)
  private List<Image> imageList = new ArrayList<>();

  // ===연관 관계 보조 메서드===//
  public void setInfluencer(Influencer influencer) {
    this.influencer = influencer;
  }

  // ===연관관계 편의 메서드===//
  public void addImage(Image image) {
    if (this.imageList.contains(image)) {
      imageList.remove(image);
    }

    image.setMedia(this);
    this.imageList.add(image);
  }

  public void addMediaHashTag() {}
}
