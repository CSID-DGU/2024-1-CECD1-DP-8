package com.cecd.dp.domain.api.report.repository;

import com.cecd.dp.domain.api.report.dto.response.ReportMediaResponseDto;

public interface ReportRepositoryCustom {

    ReportMediaResponseDto getReportMedias(Long influencerId);

}
