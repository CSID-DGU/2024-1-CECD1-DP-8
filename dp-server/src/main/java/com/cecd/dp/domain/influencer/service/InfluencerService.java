package com.cecd.dp.domain.influencer.service;

import com.cecd.dp.domain.influencer.dto.GetInfluencerReportDTO;
import com.cecd.dp.domain.influencer.dto.MostPostsProjection;
import com.cecd.dp.domain.influencer.dto.ProfileProjection;
import com.cecd.dp.domain.influencer.entity.Influencer;
import com.cecd.dp.domain.influencer.repository.InfluencerRepository;
import com.cecd.dp.domain.media.dto.MediaChartProjection;
import com.cecd.dp.domain.media.repository.MediaRepository;
import com.cecd.dp.domain.meta.entity.Meta;
import com.cecd.dp.domain.meta.repository.MetaRepository;
import com.cecd.dp.global.common.code.status.ErrorStatus;
import com.cecd.dp.global.common.exception.handler.InfluencerHandler;
import java.util.List;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

@Service
public class InfluencerService {

  private final InfluencerRepository influencerRepository;
  private final MetaRepository metaRepository;
  private final MediaRepository mediaRepository;

  public InfluencerService(
      InfluencerRepository influencerRepository,
      MetaRepository metaRepository,
      MetaRepository metaRepository1,
      MediaRepository mediaRepository) {
    this.influencerRepository = influencerRepository;
    this.metaRepository = metaRepository1;
    this.mediaRepository = mediaRepository;
  }

  public GetInfluencerReportDTO getReport(Long influencerId, String period) {

    Influencer influencer =
        influencerRepository
            .findById(influencerId)
            .orElseThrow(() -> new InfluencerHandler(ErrorStatus._NOT_FOUND_USER));

    // 프로필 정도
    ProfileProjection profile =
        influencerRepository.getProfileById(influencerId, PageRequest.of(0, 1)).get(0);

    // 인기 게시물 3개의 고유 코드
    List<MostPostsProjection> mostCodes = influencerRepository.getMostThreePostsCodesById(influencerId, PageRequest.of(0,3));

    // 인플루언서 모든 게시물의 모든 해시태그 이름 (DISTINCT)
    List<String> allTagsOfMedias = influencerRepository.getAllTagNamesById(influencerId);

    // 반응 지수
    List<Float> reactionQuotient =
        influencerRepository.calculateReactionQuotientById(influencerId, PageRequest.of(0, 1));

    // 최근 7일 게시물 좋아요 평균
    Float currentWeekLikeAvg = influencerRepository.getCurrentWeekLikeAvgById(influencerId);

    // 최근 7일 댓글 좋아요 평균
    Float currentWeekCommentsAvg = influencerRepository.getCurrentWeekCommentsAvgById(influencerId);

    Meta latestMeta =
        metaRepository.findMetaByInfluencerId(influencerId, PageRequest.of(0, 1)).get(0);

    Float likeAvg = latestMeta.getLikeAvg();
    Float commentsAvg = latestMeta.getCommentsAvg();

    Float adMediaRatio = mediaRepository.calculateAdMediaPercentageByInfluencerId(influencerId);
    Float reelsRatio = mediaRepository.calculateReelsMediaPercentageByInfluencerId(influencerId);

    // Chart 관련

    List<MediaChartProjection> reelsChartComments = null;
    List<MediaChartProjection> reelsChartLikes = null;

    if (period.equals("W")) {
      reelsChartComments = mediaRepository.getReelsChartCommentsByWeek(influencerId);
      reelsChartLikes = mediaRepository.getReelsChartLikesByWeek(influencerId);
    } else if (period.equals("D")) {
      reelsChartComments = mediaRepository.getReelsChartCommentsByDay(influencerId);
      reelsChartLikes = mediaRepository.getReelsChartLikesByDay(influencerId);
    }

    return GetInfluencerReportDTO.builder()
        .profile(profile)
        .mostThreePostsCodes(mostCodes)
        .allTagsOfMedias(allTagsOfMedias)
        .reactionQuotient(reactionQuotient)
        .currentWeekLikeAvg(currentWeekLikeAvg)
        .currentWeekCommentsAvg(currentWeekCommentsAvg)
        .likeAvg(likeAvg)
        .commentsAvg(commentsAvg)
        .adMediaRatio(adMediaRatio)
        .reelsRatio(reelsRatio)
        .reelsChartComments(reelsChartComments)
        .reelsChartLikes(reelsChartLikes)
        .build();
  }
}
