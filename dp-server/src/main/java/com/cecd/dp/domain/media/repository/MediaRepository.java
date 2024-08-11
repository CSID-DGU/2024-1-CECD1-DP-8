package com.cecd.dp.domain.media.repository;

import com.cecd.dp.domain.media.entity.Media;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MediaRepository extends JpaRepository<Media, Long> {
}
