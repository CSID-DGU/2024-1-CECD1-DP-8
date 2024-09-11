package com.cecd.dp.domain.influencer.repository;

import com.cecd.dp.domain.influencer.entity.Influencer;
import org.springframework.data.jpa.repository.JpaRepository;

public interface InfluencerRepository extends JpaRepository<Influencer, Long> {
}
