Block storage and object storage performance limits on |brand-name|
===================================================================

On |brand-name|, there are performance limits for **HDD**, **NVMe (SSD)**, and **Object Storage** to ensure stable operation and protect against accidental DDoS attacks.

Current limits
--------------

Block HDD
   **500** IOPS (read and write)

Block SSD/NVMe
   **3000** IOPS (read and write)

   **NOTE**: On |brand-name|, *all* SSD storage is NVMe-based.

S3 Object Storage (General Tier)
   **2000** operations per second with a

   * **2500 burst limit** per bucket and
   * **150 MB/s** transfer per request

In majority of cases, the actual throughput may be larger because:

 * Typical downloads use **multiple requests** and
 * More than **99.95%** of requests stay below **100 MB/s**.

Again, this limit primarily helps mitigate accidental **DDoS** scenarios.