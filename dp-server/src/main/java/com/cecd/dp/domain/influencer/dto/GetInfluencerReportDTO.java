package com.cecd.dp.domain.influencer.dto;

import java.util.List;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class GetInfluencerReportDTO {

  private ProfileProjection profile;
  private List<MostPostsProjection> mostThreePosts;
  private List<String> allTagsOfMedias;
  private List<Float> reactionQuotient;
  private Float currentWeekLikeAvg;
  private Float currentWeekCommentsAvg;
  private Float likeAvg;
  private Float commentsAvg;
  private Float adMediaRatio;
  private Float reelsRatio;
}
