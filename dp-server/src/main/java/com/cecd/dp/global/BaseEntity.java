package com.cecd.dp.global;

import jakarta.persistence.EntityListeners;
import jakarta.persistence.MappedSuperclass;
import java.time.LocalDateTime;
import lombok.Getter;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
@Getter
public abstract class BaseEntity {

  // row 생성시간
  @CreatedDate private LocalDateTime createdAt;

  // row 업데이트 시간
  @LastModifiedDate private LocalDateTime updatedAt;
}
