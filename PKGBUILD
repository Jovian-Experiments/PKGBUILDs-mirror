# Maintainer: Thomas Bächler <thomas@archlinux.org>

pkgbase=linux-firmware-neptune
pkgname=(linux-firmware-neptune-whence linux-firmware-neptune  amd-ucode
         linux-firmware-{nfp,mellanox,marvell,qcom,liquidio,qlogic,bnx2x}
)
_tag=jupiter-20240605.1
pkgver=${_tag//-/.}
pkgrel=1
pkgdesc="Firmware files for Linux"
url="https://gitlab.steamos.cloud/jupiter/linux-firmware-neptune"
license=('GPL2' 'GPL3' 'custom')
arch=('any')
makedepends=('git' 'openssh')
options=(!strip)
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/linux-firmware-neptune.git#tag=$_tag"
         0001-Add-support-for-compressing-firmware-in-copy-firmware.patch)
sha256sums=('SKIP'
            'b7feb7db71160e9fe6f3114405e6ab883abfb12a540c8b6a2a7088295dcf5bd2')
validpgpkeys=('4CDE8575E547BF835FE15807A31B6BD72486CFD6') # Josh Boyer <jwboyer@fedoraproject.org>

_backports=(
)

prepare() {
  cd ${pkgbase}

  local _c
  for _c in "${_backports[@]}"; do
    git log --oneline -1 "${_c}"
    git cherry-pick -n "${_c}"
  done

  # add firmware compression support - patch taken from Fedora
  patch -Np1 -i ../0001-Add-support-for-compressing-firmware-in-copy-firmware.patch
}

build() {
  mkdir -p kernel/x86/microcode
  cat ${pkgbase}/amd-ucode/microcode_amd*.bin > kernel/x86/microcode/AuthenticAMD.bin

  # Reproducibility: set the timestamp on the bin file
  if [[ -n ${SOURCE_DATE_EPOCH} ]]; then
    touch -d @${SOURCE_DATE_EPOCH} kernel/x86/microcode/AuthenticAMD.bin
  fi

  # Reproducibility: strip the inode and device numbers from the cpio archive
  echo kernel/x86/microcode/AuthenticAMD.bin |
    bsdtar --uid 0 --gid 0 -cnf - -T - |
    bsdtar --null -cf - --format=newc @- > amd-ucode.img
}

_pick() {
  local p="$1" f d; shift
  for f; do
    d="$srcdir/$p/${f#$pkgdir/}"
    mkdir -p "$(dirname "$d")"
    mv "$f" "$d"
    rmdir -p --ignore-fail-on-non-empty "$(dirname "$f")"
  done
}

package_linux-firmware-neptune-whence() {
  pkgdesc+=" - contains the WHENCE license file which documents the vendor license details"
  provides=('linux-firmware-whence')
  conflicts=('linux-firmware-whence')
  replaces=('linux-firmware-whence')

  install -Dt "${pkgdir}/usr/share/licenses/${pkgname}" -m644 ${pkgbase}/WHENCE
}

package_linux-firmware-neptune() {
  depends=('linux-firmware-whence')
  provides=('linux-firmware')
  conflicts=('linux-firmware')
  replaces=('linux-firmware')

  cd ${pkgbase}

  ZSTD_CLEVEL=19 make DESTDIR="${pkgdir}" FIRMWAREDIR=/usr/lib/firmware installcompress

  # Trigger a microcode reload for configurations not using early updates
  echo 'w /sys/devices/system/cpu/microcode/reload - - - - 1' |
    install -Dm644 /dev/stdin "${pkgdir}/usr/lib/tmpfiles.d/${pkgname}.conf"

  install -Dt "${pkgdir}/usr/share/licenses/${pkgname}" -m644 LICEN*

  # split
  cd "${pkgdir}"

  _pick linux-firmware-nfp usr/lib/firmware/netronome
  _pick linux-firmware-nfp usr/share/licenses/${pkgname}/LICENCE.Netronome

  _pick linux-firmware-mellanox usr/lib/firmware/mellanox

  _pick linux-firmware-marvell usr/lib/firmware/{libertas,mwl8k,mwlwifi,mrvl}
  _pick linux-firmware-marvell usr/share/licenses/${pkgname}/LICENCE.{Marvell,NXP}

  _pick linux-firmware-qcom usr/lib/firmware/{qcom,a300_*}
  _pick linux-firmware-qcom usr/share/licenses/${pkgname}/LICENSE.qcom*

  _pick linux-firmware-liquidio usr/lib/firmware/liquidio
  _pick linux-firmware-liquidio usr/share/licenses/${pkgname}/LICENCE.cavium_liquidio

  _pick linux-firmware-qlogic usr/lib/firmware/{qlogic,qed,ql2???_*,c{b,t,t2}fw-*}
  _pick linux-firmware-qlogic usr/share/licenses/${pkgname}/LICENCE.{qla1280,qla2xxx}

  _pick linux-firmware-bnx2x usr/lib/firmware/bnx2x*
}

package_amd-ucode() {
  pkgdesc="Microcode update image for AMD CPUs"
  license=(custom)

  install -Dt "${pkgdir}/boot" -m644 amd-ucode.img

  install -Dt "${pkgdir}/usr/share/licenses/${pkgname}" -m644 ${pkgbase}/LICENSE.amd-ucode
}

package_linux-firmware-nfp() {
  pkgdesc+=" - nfp / Firmware for Netronome Flow Processors"
  depends=('linux-firmware-whence')

  mv -v linux-firmware-nfp/* "${pkgdir}"
}

package_linux-firmware-mellanox() {
  pkgdesc+=" - mellanox / Firmware for Mellanox Spectrum switches"
  depends=('linux-firmware-whence')

  mv -v linux-firmware-mellanox/* "${pkgdir}"
}

package_linux-firmware-marvell() {
  pkgdesc+=" - marvell / Firmware for Marvell devices"
  depends=('linux-firmware-whence')

  mv -v linux-firmware-marvell/* "${pkgdir}"
  # remove arm64 firmware #76583
  rm -rf "${pkgdir}"/usr/lib/firmware/mrvl/prestera/mvsw_prestera_fw_arm64-v4.1.img.xz
}

package_linux-firmware-qcom() {
  pkgdesc+=" - qcom / Firmware for Qualcomm SoCs"
  depends=('linux-firmware-whence')

  mv -v linux-firmware-qcom/* "${pkgdir}"
}

package_linux-firmware-liquidio() {
  pkgdesc+=" - liquidio / Firmware for Cavium LiquidIO server adapters"
  depends=('linux-firmware-whence')

  mv -v linux-firmware-liquidio/* "${pkgdir}"
}

package_linux-firmware-qlogic() {
  pkgdesc+=" - qlogic / Firmware for QLogic devices"
  depends=('linux-firmware-whence')

  mv -v linux-firmware-qlogic/* "${pkgdir}"
}

package_linux-firmware-bnx2x() {
  pkgdesc+=" - bnx2x / Firmware for Broadcom NetXtreme II 10Gb ethernet adapters"
  depends=('linux-firmware-whence')

  mv -v linux-firmware-bnx2x/* "${pkgdir}"
}

# vim:set sw=2 et:
