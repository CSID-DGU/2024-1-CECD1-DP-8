package com.cecd.dp.domain.api.report.repository;

import com.cecd.dp.domain.api.report.dto.response.ReportTagResponseDto;
import com.cecd.dp.domain.api.report.dto.response.SummaryResponseDto;
import org.springframework.stereotype.Repository;

import java.util.Optional;

public interface ReportHashTagRepositoryCustom {

    ReportTagResponseDto getAllDistinctTagList(Long influencerId);

    Optional<SummaryResponseDto> getSummaryThisMonth(Long influencerId);
}
