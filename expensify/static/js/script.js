(function() {

  $(document).ready(function() {
    return $(".nav li").removeClass("active").find("a[href='" + window.location.pathname + "']").closest("li").addClass("active");
  });

  $(".mark_as_claimed").live({
    click: function(e) {
      var cb, selected_claims, _i, _len, _ref;
      e.preventDefault();
      $("[name='mark_as']").val("True");
      selected_claims = "";
      _ref = $(".cb_claims");
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        cb = _ref[_i];
        if ($(cb).attr("checked")) selected_claims += cb.id + ";";
      }
      selected_claims = selected_claims.substr(0, selected_claims.length - 1);
      $("[name='selected']").val(selected_claims);
      return $(this).closest('form').submit();
    }
  });

  $(".mark_as_not_claimed").live({
    click: function(e) {
      var cb, selected_claims, _i, _len, _ref;
      e.preventDefault();
      $("[name='mark_as']").val("False");
      selected_claims = "";
      _ref = $(".cb_claims");
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        cb = _ref[_i];
        if ($(cb).attr("checked")) selected_claims += cb.id + ";";
      }
      selected_claims = selected_claims.substr(0, selected_claims.length - 1);
      $("[name='selected']").val(selected_claims);
      return $(this).closest('form').submit();
    }
  });

  $("#check_all").live({
    click: function() {
      if ($(this).attr("checked")) {
        return $("[type='checkbox']").attr("checked", "checked");
      } else {
        return $("[type='checkbox']").removeAttr("checked");
      }
    }
  });

}).call(this);
