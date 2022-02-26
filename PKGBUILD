# Maintainer: Your Name <youremail@domain.com>
pkgname=jupiter-legacy-support
pkgver=1.106
pkgrel=1
pkgdesc="Legacy support files from foxnet that haven't been split to their own thing"
arch=(any)
depends=(python3 python-psutil python-aiohttp nvme-cli)
source=(jupiter-factoryinstall
        jupiter-plasma-bootstrap
        jupiter-plasma-bootstrap.desktop
        steam-web-debug-portforward.service
        91-dracut-install-vanilla.hook
        killuserprocesses.conf
        flatpak-workaround.service
        flathub-beta.flatpakrepo
        black_800x1280.png
        white_800x1280.png)
sha256sums=('60921ba59c5b1923264e7aa931eb86ff0b55d09df390f429993b76269ee6f1a0'
            '9e9e4884a64eb4eb784305d932726ab89beee0edd60600f9b13878cea7a7671f'
            '9ca42095d379a8b8089cd704c2351cc36a0c85cfc0813fcbb3aebd35105f1365'
            '1d4af38d96614a784a2617b530f26c85d7fb34fd0e97a013a3502b90d61d0ce2'
            '78b1749684bf3c60a5769002d98008772145385566ab68d7218c3850ec2dc653'
            'e34a9dc905771bd99cd04cdf88262481cab7a7808d99dfaa968366fcb1b99a0b'
            '608a3132b952022282ff1219d61acc627c58500e12033cc223c2327d6ee89c3c'
            '582cae3c9f9d4639f027defafe6fa33bda0a3a4d441290d926ad85a2be0f7206'
            '942fbb9436835bdb3a87aa8d73b3461f4cee0bc2f58bfa308eeb1be6b52ccb39'
            'fd55e252b11a0b0d48b7147298f159b0470f29ccb6118a79a5692cc8c4635f5b')

package() {
  # Hacky -- this package isn't proper and just references the salt files it owns.
  # Everything in here needs to be split into proper packaging and this package obsoleted.
  cd "$startdir"/saltfiles/

  install -D -m644 "$srcdir"/black_800x1280.png "$pkgdir"/usr/share/jupiter_testing/black_800x1280.png
  install -D -m644 "$srcdir"/white_800x1280.png "$pkgdir"/usr/share/jupiter_testing/white_800x1280.png

  # flathub workaround and beta repo
  install -D -m644 "$srcdir"/flathub-beta.flatpakrepo "$pkgdir"/etc/flatpak/remotes.d/flathub-beta.flatpakrepo
  install -D -m644 "$srcdir"/flatpak-workaround.service "$pkgdir"/usr/lib/systemd/system/flatpak-workaround.service
  install -d "$pkgdir"/usr/lib/systemd/system/multi-user.target.wants/
  ln -sv ../flatpak-workaround.service "$pkgdir"/usr/lib/systemd/system/multi-user.target.wants/

  # Plasma autostart helper
  install -D -m755 "$srcdir"/jupiter-plasma-bootstrap "$pkgdir"/usr/bin/jupiter-plasma-bootstrap
  install -D -m644 "$srcdir"/jupiter-plasma-bootstrap.desktop "$pkgdir"/etc/xdg/autostart/jupiter-plasma-bootstrap.desktop

  install -D -m644 "$srcdir"/killuserprocesses.conf "$pkgdir"/etc/systemd/logind.conf.d/killuserprocesses.conf

  install -D -m644 "$srcdir"/91-dracut-install-vanilla.hook "$pkgdir"/usr/share/libalpm/hooks/91-dracut-install-vanilla.hook

  install -D -m644 "$srcdir"/steam-web-debug-portforward.service "$pkgdir"/etc/systemd/system/steam-web-debug-portforward.service

  install -D -m755 "$srcdir"/jupiter-factoryinstall "$pkgdir"/usr/bin/jupiter-factoryinstall
  install -D -m644 xbindkeysrc "$pkgdir"/etc/xbindkeysrc

  # Stats daemon will be enabled/started by bootstrap

  install -D -m755 -t "$pkgdir"/usr/bin/ usr/bin/*

  install -D -m644 {,"$pkgdir"/}usr/share/X11/xorg.conf.d/41-touchscreenrotate.conf

  install -D -m644 {,"$pkgdir"/}usr/share/xsessions/plasma-steamos-oneshot.desktop

  install -D -m644 {,"$pkgdir"/}etc/sddm.conf.d/steamos.conf
  # install -D -m644 {,"$pkgdir"/}etc/pulse/default.pa
  install -D -m644 {,"$pkgdir"/}etc/sysctl.d/swappiness.conf

  # FIXME reconcile with grub-steamos
  install -D -m644 etc/default/grub "$pkgdir"/etc/default/grub-legacy

  install -D -m644 {,"$pkgdir"/}etc/systemd/system/NetworkManager.service.d/override.conf
  install -D -m644 {,"$pkgdir"/}etc/systemd/system.conf.d/foxnet-system.conf
  install -D -m644 {,"$pkgdir"/}etc/systemd/logind.conf.d/suspendbutton.conf

  # Workaround -- disable Holo's /var/boot mechanics entirely.  They're broken in a number of ways and are bricking
  # units.  The feature it's trying to enable (DKMS?) isn't even relevant at the moment.
  #
  # Symlinking to /dev/null is actually what `systemctl mask` does. Really.
  ln -sv /dev/null "$pkgdir"/etc/systemd/system/boot.mount
  ln -sv /dev/null "$pkgdir"/etc/systemd/system/steamos-mkvarboot.service
  ln -sv /dev/null "$pkgdir"/etc/systemd/system/steamos-install-grub.service

  # Horrible workaround. We should fix this.
  # (the full bootstrap package should not need this)
  mkdir -m755 -p "$pkgdir"/usr/share/fonts/truetype/ttf-dejavu
  ln -sv ../../TTF/DejaVuSans.ttf "$pkgdir"/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf

  # Non-saltfiles
  mkdir -p -m755 "$pkgdir"/etc/systemd/system/sound.target.wants
  mkdir -p -m755 "$pkgdir"/etc/systemd/system/multi-user.target.wants
}
