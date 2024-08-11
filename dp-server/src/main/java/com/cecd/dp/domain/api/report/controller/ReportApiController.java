package com.cecd.dp.domain.api.report.controller;

import com.cecd.dp.domain.api.report.dto.response.ReportResponseDto;
import com.cecd.dp.domain.api.report.service.ReportService;
import com.cecd.dp.global.common.ApiResponse;
import io.swagger.v3.oas.annotations.Operation;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/reports")
@RequiredArgsConstructor
public class ReportApiController {

    private final ReportService reportService;

    @Operation(summary = "인플루언서 리포트 API", description = "인플루언서 리포팅 페이지에 보여줄 모든 데이터")
    @GetMapping("/{influencerId}")
    public ApiResponse<ReportResponseDto> getReport(
            @PathVariable(name = "influencerId") Long influencerId
    ) {
        return ApiResponse.onSuccess(reportService.getReport(influencerId));
    }
}
