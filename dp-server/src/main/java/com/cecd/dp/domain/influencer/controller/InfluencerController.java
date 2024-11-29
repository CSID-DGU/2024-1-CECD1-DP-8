package com.cecd.dp.domain.influencer.controller;

import com.cecd.dp.domain.influencer.dto.GetHashTagReportDTO;
import com.cecd.dp.domain.influencer.dto.GetInfluencerReportDTO;
import com.cecd.dp.domain.influencer.service.InfluencerService;
import com.cecd.dp.global.common.ApiResponse;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/influencer")
@Tag(name = "Influencer", description = "인플루언서 관련 API")
public class InfluencerController {

  private final InfluencerService influencerService;

  public InfluencerController(InfluencerService influencerService) {
    this.influencerService = influencerService;
  }

  @Operation(summary = "인플루언서 리포트 조회 API", description = "특정 인플루언서의 리포트 내역을 조회합니다.")
  @GetMapping("/report/{id}")
  // TODO: period가 W 와 D 만 받도록 글로벌 예외처리 어
  public ApiResponse<?> getReport(
      @PathVariable(name = "id") String id, @RequestParam("period") String period) {

    GetInfluencerReportDTO report = null;

    if (isNumeric(id)) {
      report = influencerService.getReportByLongId(Long.parseLong(id), period);
    } else {
      report = influencerService.getReportByStringId(id, period);
    }

    return ApiResponse.onSuccess(report);
  }

  /**
   * * 최근 50개의 게시물들의 해시태그들을 분석합니다.
   *
   * @param id
   * @return maxEngagement, avgEngagement, usageCount, totalEngagement OF hash_tag_name
   */
  @Operation(
      summary = "인플루언서의 최근 50개 게시물 해시태그 리포트 조회 API",
      description = "최근 50개의 게시물에 담긴 해시태그들의 engagement들과 사용횟수를 반환합니다.")
  @GetMapping("/report/hash-tags/{id}")
  public ApiResponse<?> getHashTagReport(@PathVariable(name = "id") Long id) {
    GetHashTagReportDTO hashTagReport = influencerService.getHashTagReport(id);

    return ApiResponse.onSuccess(hashTagReport);
  }

  private boolean isNumeric(String str) {
    try {
      Long.parseLong(str);
      return true;
    } catch (NumberFormatException e) {
      return false;
    }
  }
}
