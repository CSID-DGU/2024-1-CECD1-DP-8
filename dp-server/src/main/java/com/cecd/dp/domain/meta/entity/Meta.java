package com.cecd.dp.domain.meta.entity;

import com.cecd.dp.domain.influencer.entity.Influencer;
import com.cecd.dp.global.BaseEntity;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
public class Meta {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  @Column(name = "meta_id")
  private Long id;

  // 평균 좋아요 수
  private Integer likeAvg;

  // 평균 댓글 수
  private Integer commentsAvg;

  // 팔로워 수
  private Integer followerCnt;

  // 팔로잉 수
  private Integer followsCnt;

  // 수집 날짜
  private LocalDateTime postedAt;

  @ManyToOne(fetch = FetchType.LAZY)
  @JoinColumn(name = "influencer_id")
  private Influencer influencer;

  public void setInfluencer(Influencer influencer) {
    this.influencer = influencer;
  }
}
