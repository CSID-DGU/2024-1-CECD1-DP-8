package com.cecd.dp.domain.api.report.service;

import com.cecd.dp.domain.api.report.dto.response.ReportMediaResponseDto;
import com.cecd.dp.domain.api.report.dto.response.ReportProfileResponseDto;
import com.cecd.dp.domain.api.report.dto.response.ReportResponseDto;
import com.cecd.dp.domain.api.report.dto.response.ReportTagResponseDto;
import com.cecd.dp.domain.influencer.entity.Influencer;
import com.cecd.dp.domain.influencer.repository.InfluencerRepository;
import com.cecd.dp.domain.media.repository.MediaRepositoryCustom;
import com.cecd.dp.global.common.code.status.ErrorStatus;
import com.cecd.dp.global.common.exception.handler.InfluencerHandler;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
@Transactional(readOnly = true)
public class ReportService {
    private final InfluencerRepository influencerRepository;
    private final MediaRepositoryCustom mediaRepositoryCustom;

    public ReportResponseDto getReport(Long influencerId) {

        Influencer influencer = influencerRepository.findById(influencerId)
                .orElseThrow(() -> new InfluencerHandler(ErrorStatus._NOT_FOUND_USER));

        ReportResponseDto reportResponseDto = ReportResponseDto.builder()
                .profile(ReportProfileResponseDto.fromInfluencer(influencer))  // 프로필 데이터
                .mediaList(ReportMediaResponseDto.fromMediaList(influencer.getMediaList())) // 인기 포스트 3개
                .tagList(ReportTagResponseDto.fromMediaList(influencer.getMediaList()))  // 인플루언서의 모든 게시글의 distinct 해시태크 목록
                .highResponseTag(null) // 인기 포스트에서의 해시태그 목록(제일 인기 -> 3개 해시태그?)
                .likeAvg(influencer.getLatestMeta().getLikeAvg()) // 최근 평균 좋아요 수
                .replyAvg(influencer.getLatestMeta().getReplyAvg()) // 최근 평균 댓글 수
                .mediaUploadCycle(mediaRepositoryCustom.calculateMediaUploadCycle(influencerId)) // 게시글 업로드 주기(per week)
                .summary(null) // Summary
                .build();

        return reportResponseDto;
    }
}
