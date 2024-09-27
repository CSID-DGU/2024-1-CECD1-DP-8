package com.cecd.dp.domain.influencer.controller;

import com.cecd.dp.domain.influencer.service.InfluencerService;
import com.cecd.dp.global.common.ApiResponse;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

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
    public ApiResponse<?> getReport(@PathVariable(name = "id") Long influencerId) {
        return ApiResponse.onSuccess(influencerService.getReport(influencerId));
    }

}
