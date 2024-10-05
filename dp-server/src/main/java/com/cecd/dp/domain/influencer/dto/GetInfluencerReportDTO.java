package com.cecd.dp.domain.influencer.dto;

import com.cecd.dp.domain.media.dto.MediaChartProjection;
import java.util.List;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class GetInfluencerReportDTO {

  private ProfileProjection profile;
  private List<MostPostsProjection> mostThreePostsCodes;
  private List<String> allTagsOfMedias;
  private List<Float> reactionQuotient;
  private Float currentWeekLikeAvg;
  private Float currentWeekCommentsAvg;
  private Float likeAvg;
  private Float commentsAvg;
  private Float adMediaRatio;
  private Float reelsRatio;
  private List<MediaChartProjection> reelsChartComments;
  private List<MediaChartProjection> reelsChartLikes;
}
