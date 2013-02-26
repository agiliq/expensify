(function() {

  $(document).ready(function() {
    return $(".nav li").removeClass("active").find("a[href='" + window.location.pathname + "']").closest("li").addClass("active");
  });

  $(".action_button").live({
    click: function(e) {
      var cb, selected_claims, _i, _len, _ref;
      e.preventDefault();
      if ($(this).attr("action") === "mark_as_claimed") {
        $("[name='mark_as']").val("True");
      } else if ($(this).attr("action") === "rejected") {
        $("[name='mark_as']").val("rejected");
      }
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
  }, $(".expense-list tr").live({
    click: function(e) {
      var id, url_name_arr;
      e.preventDefault();
      id = e.id;
      if ($(".field_name").length > 0) {
        $(".td_name").text($(this).find(".field_name").text());
      }
      $(".td_category").text($(this).find(".field_category").text());
      $(".td_amount").text($(this).find(".field_amount").text());
      $(".td_date").text($(this).find(".field_date").text());
      $(".td_status").text($(this).find(".field_status").text());
      $(".td_description").text($(this).find(".description").val());
      if ($(this).find(".invoice").val().trim().length > 0) {
        url_name_arr = $(this).find(".invoice").val().split(";");
        $(".td_invoice").html("<a href='" + url_name_arr[0] + "' target='_blank' >" + url_name_arr[1] + "</a>");
      } else {
        $(".td_invoice").text("Not provided");
      }
      return $("#expense-detail").modal();
    }
  }));

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
