package com.cecd.dp.domain.influencer.controller;

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
  //TODO: period가 W 와 D 만 받도록 글로벌 예외처리 어노테이션으로 구현
  public ApiResponse<?> getReport(@PathVariable(name = "id") Long influencerId, @RequestParam("period") String period) {
    return ApiResponse.onSuccess(influencerService.getReport(influencerId, period));
  }
}
